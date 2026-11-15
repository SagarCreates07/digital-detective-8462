# Mission 7 — How computers communicate

## 1. Task / objective
The mission asked me to explain basic network types and concepts, observe network lookup and connectivity information using Terminal, and describe what happens when a website opens.

## 2. Work completed
I filled in a table of eight networking concepts with examples. I ran a connectivity test and a DNS lookup on a public example website, and I wrote a step-by-step explanation of what happens when I open a website.

### Task 7.1 — Network concepts

| Concept | Explanation in my own words | Example |
|---|---|---|
| LAN | A network that connects devices in one small place | The Wi-Fi at home or in my college lab |
| MAN | A network that covers a whole city or a large campus | Several buildings of one university joined into one network |
| WAN | A network that covers a very large area, like countries or continents | The internet |
| DNS | It turns a website name into the number address of the computer that hosts it | Typing a website name and the computer finding that website |
| Router | A device that passes data between networks and sends it the right way | The box at home that connects my Wi-Fi to the internet |
| Protocol | A set of rules that devices follow so they can understand each other | HTTPS, the rules my browser uses to talk to websites |
| Packet switching | Data is cut into small pieces called packets, which travel separately and are joined again at the end | Sending a large photo in a chat app |
| Client-server | One device (the client) asks for something and another device (the server) provides it | My browser asks for a web page and the website's server sends it back |

### Task 7.2 — Observe network information

**Commands used:** `ping -c 4 example.com` and `nslookup example.com`

**What I observed with ping:** I sent 4 test messages to example.com. [Write what you saw, for example: 4 replies came back, each with a time in milliseconds, and the summary said 4 packets were transmitted, 4 received and 0% packet loss.]

**What I observed with the DNS lookup:** `nslookup example.com` printed the name example.com and an address that DNS found for it. The first lines showed the DNS server used by my own network, which I have replaced with [redacted] for privacy.

**What a connectivity test helps me check:** It checks whether my computer can reach another computer over the network, and how long messages take to go there and come back. If replies come back the connection works, and if they don't, something is wrong with my internet or the website.

**What information a DNS lookup displays:** It shows the website name I asked about and the IP address that belongs to it. It also shows which DNS server answered.

**The role of DNS when I enter a website name:** Computers find each other using IP addresses, not names. When I type a website name in the browser, DNS looks up the IP address for that name, and then my browser can connect to the right server.

### Task 7.3 — What happens when I open a website?

1. I type a website name, like example.com, into my browser and press Enter. My computer and its browser act as the **client**, because they are the ones asking for the page.
2. The browser does not know where example.com is, so it asks **DNS**. DNS looks up the name and gives back the IP address of the computer that hosts the website.
3. The browser prepares a request using a **protocol**, usually HTTPS, which is the set of rules browsers and websites follow to understand each other.
4. The request leaves my computer and goes to my router. The router sends it out of my local network towards the internet.
5. The request travels across many networks, split into small packets, until it reaches the **server** that hosts the website.
6. The server finds the web page and sends it back to my computer as a response, again as packets that travel through routers and are joined together at my end.
7. My browser puts the packets together, builds the page, and shows it on my screen.

## 3. Commands / tools used
- `ping -c 4 example.com`: sends 4 test messages to a website to check that my computer can reach it
- `nslookup example.com`: asks DNS for the address that belongs to a website name
- Tools: Terminal and VS Code

## 4. My understanding
A computer network connects devices so they can share data and resources. A LAN covers a small place, a MAN covers a city or campus, and a WAN covers a very large area, like the internet. DNS turns website names into IP addresses, a router passes data between networks, and a protocol is a set of rules that devices follow to understand each other. Data travels in small packets, and the client-server idea means one device asks and another answers. When I open a website, my browser asks DNS for the address, sends a request through my router to the server, and the server sends the page back to be shown on my screen.

## 5. Difficulties faced
When I ran `nslookup example.com`, the first lines of the output showed the DNS server of my own network. I was not sure whether I could publish them.

## 6. How I resolved them
The assignment says not to publish network details, so I replaced those lines with [redacted] and only described the lines about example.com.

## 7. Evidence / files
- README.md in mission-07-networking, containing the concept table, the observations and the website explanation
- No IP address, Wi-Fi name or device name of mine is included

## 8. Commit details
Commit message: "Explain networking concepts and website communication"
The work was pushed to GitHub and the commit is visible there.