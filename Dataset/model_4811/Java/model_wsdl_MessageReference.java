





import java.util.List;
import java.util.ArrayList;

public class model_wsdl_MessageReference extends ExtensibleElement {

    private String name;





    private Message message;


    public model_wsdl_MessageReference(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Message getMessage() {
        return message;
    }

    public void setMessage(Message message) {
        this.message = message;
    }

}