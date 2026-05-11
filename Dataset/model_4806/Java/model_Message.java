





import java.util.List;
import java.util.ArrayList;

public class model_Message  {

    private String avgResponseTime;
    private String messageSize;
    private String timestamp;
    private String name;
    private String uid;





    private model_ServiceInstance model_serviceinstance;




    private model_ServiceInstance model_serviceinstance;




    private model_ServiceInstance model_serviceinstance;


    public model_Message(
        String avgResponseTime,        String messageSize,        String timestamp,        String name,        String uid    ) {
        this.avgResponseTime = avgResponseTime;
        this.messageSize = messageSize;
        this.timestamp = timestamp;
        this.name = name;
        this.uid = uid;
    }


    public String getAvgresponsetime() {
        return avgResponseTime;
    }

    public void setAvgresponsetime(String avgResponseTime) {
        this.avgResponseTime = avgResponseTime;
    }
    public String getMessagesize() {
        return messageSize;
    }

    public void setMessagesize(String messageSize) {
        this.messageSize = messageSize;
    }
    public String getTimestamp() {
        return timestamp;
    }

    public void setTimestamp(String timestamp) {
        this.timestamp = timestamp;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getUid() {
        return uid;
    }

    public void setUid(String uid) {
        this.uid = uid;
    }

    public model_ServiceInstance getModel_serviceinstance() {
        return model_serviceinstance;
    }

    public void setModel_serviceinstance(model_ServiceInstance model_serviceinstance) {
        this.model_serviceinstance = model_serviceinstance;
    }
    public model_ServiceInstance getModel_serviceinstance() {
        return model_serviceinstance;
    }

    public void setModel_serviceinstance(model_ServiceInstance model_serviceinstance) {
        this.model_serviceinstance = model_serviceinstance;
    }
    public model_ServiceInstance getModel_serviceinstance() {
        return model_serviceinstance;
    }

    public void setModel_serviceinstance(model_ServiceInstance model_serviceinstance) {
        this.model_serviceinstance = model_serviceinstance;
    }

}