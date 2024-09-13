<template>
  <div>
    <h1>WebSocket Chat</h1>
    <div class="messages">
      <div v-for="(message, index) in messages" :key="index">
        {{ message }}
      </div>
    </div>
    <input v-model="newMessage" placeholder="Type a message..." />
    <button @click="sendMessage">Send</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      ws: null,
      messages: [],
      newMessage: "",
    };
  },
  created() {
    this.connectWebSocket();
  },
  methods: {
    connectWebSocket() {
      // URL do WebSocket que passa pelo seu API Gateway
      this.ws = new WebSocket("ws://localhost:8000/api/gateway/ws/chat/");

      this.ws.onmessage = (event) => {
        this.messages.push(event.data);
      };

      this.ws.onerror = (error) => {
        console.error("WebSocket error:", error);
      };

      this.ws.onclose = () => {
        console.log("WebSocket closed, trying to reconnect...");
        setTimeout(this.connectWebSocket, 1000); // Reconnect after 1s
      };
    },
    sendMessage() {
      if (this.newMessage) {
        this.ws.send(this.newMessage);
        this.newMessage = "";
      }
    },
  },
};
</script>

<style scoped>
.messages {
  border: 1px solid #ccc;
  height: 300px;
  overflow-y: scroll;
  margin-bottom: 10px;
}
input {
  width: calc(100% - 60px);
}
button {
  width: 50px;
}
</style>
