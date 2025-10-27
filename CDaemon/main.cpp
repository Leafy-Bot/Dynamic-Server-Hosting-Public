#include <iostream>
#include <cstdlib>
#include <httplib.h>

int main() {
    httplib::Server svr;

    svr.Post("/start", [&](const httplib::Request&, httplib::Response& res) {
        std::system("docker run -d --name McTest -p 25565:25565 my-minecraft");
        res.set_content("server started", "text/plain");
    });

    svr.Post("/stop", [&](const httplib::Request&, httplib::Response& res) {
        std::system("docker stop mc-test");
        std::system("docker rm mc-test");
        res.set_content("stopped", "text/plain");
    });

    std::cout << "Agent running on port 9000\n";
    svr.listen("0.0.0.0", 9000);
}