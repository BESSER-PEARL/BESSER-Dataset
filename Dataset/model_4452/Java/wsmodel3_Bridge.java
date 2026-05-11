





import java.util.List;
import java.util.ArrayList;

public class wsmodel3_Bridge  {

    private String host;
    private int port;
    private String topic;





    private wsmodel3_MessageBroker wsmodel3_messagebroker;




    private wsmodel3_REST wsmodel3_rest;


    public wsmodel3_Bridge(
        String host,        int port,        String topic    ) {
        this.host = host;
        this.port = port;
        this.topic = topic;
    }


    public String getHost() {
        return host;
    }

    public void setHost(String host) {
        this.host = host;
    }
    public int getPort() {
        return port;
    }

    public void setPort(int port) {
        this.port = port;
    }
    public String getTopic() {
        return topic;
    }

    public void setTopic(String topic) {
        this.topic = topic;
    }

    public wsmodel3_MessageBroker getWsmodel3_messagebroker() {
        return wsmodel3_messagebroker;
    }

    public void setWsmodel3_messagebroker(wsmodel3_MessageBroker wsmodel3_messagebroker) {
        this.wsmodel3_messagebroker = wsmodel3_messagebroker;
    }
    public wsmodel3_REST getWsmodel3_rest() {
        return wsmodel3_rest;
    }

    public void setWsmodel3_rest(wsmodel3_REST wsmodel3_rest) {
        this.wsmodel3_rest = wsmodel3_rest;
    }

}