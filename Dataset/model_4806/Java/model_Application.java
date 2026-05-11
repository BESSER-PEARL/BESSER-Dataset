





import java.util.List;
import java.util.ArrayList;

public class model_Application  {

    private String totalMessages;
    private String totalData;
    private String weight;
    private String name;





    private model_StringToApplication model_stringtoapplication;


    public model_Application(
        String totalMessages,        String totalData,        String weight,        String name    ) {
        this.totalMessages = totalMessages;
        this.totalData = totalData;
        this.weight = weight;
        this.name = name;
    }


    public String getTotalmessages() {
        return totalMessages;
    }

    public void setTotalmessages(String totalMessages) {
        this.totalMessages = totalMessages;
    }
    public String getTotaldata() {
        return totalData;
    }

    public void setTotaldata(String totalData) {
        this.totalData = totalData;
    }
    public String getWeight() {
        return weight;
    }

    public void setWeight(String weight) {
        this.weight = weight;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public model_StringToApplication getModel_stringtoapplication() {
        return model_stringtoapplication;
    }

    public void setModel_stringtoapplication(model_StringToApplication model_stringtoapplication) {
        this.model_stringtoapplication = model_stringtoapplication;
    }

}