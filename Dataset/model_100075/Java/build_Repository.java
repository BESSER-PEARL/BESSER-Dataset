





import java.util.List;
import java.util.ArrayList;

public class build_Repository extends BExpression {

    private String handlerType;
    private String name;
    private String documentation;



    public build_Repository(
        String handlerType,        String name,        String documentation    ) {
        super(
        );
        this.handlerType = handlerType;
        this.name = name;
        this.documentation = documentation;
    }


    public String getHandlertype() {
        return handlerType;
    }

    public void setHandlertype(String handlerType) {
        this.handlerType = handlerType;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDocumentation() {
        return documentation;
    }

    public void setDocumentation(String documentation) {
        this.documentation = documentation;
    }


}