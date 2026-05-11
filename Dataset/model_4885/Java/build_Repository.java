





import java.util.List;
import java.util.ArrayList;

public class build_Repository extends BExpression {

    private String handlerType;
    private String documentation;
    private String name;





    private build_BuildUnit build_buildunit;




    private build_BExpression build_bexpression;


    public build_Repository(
        String handlerType,        String documentation,        String name    ) {
        super(
        );
        this.handlerType = handlerType;
        this.documentation = documentation;
        this.name = name;
    }


    public String getHandlertype() {
        return handlerType;
    }

    public void setHandlertype(String handlerType) {
        this.handlerType = handlerType;
    }
    public String getDocumentation() {
        return documentation;
    }

    public void setDocumentation(String documentation) {
        this.documentation = documentation;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public build_BuildUnit getBuild_buildunit() {
        return build_buildunit;
    }

    public void setBuild_buildunit(build_BuildUnit build_buildunit) {
        this.build_buildunit = build_buildunit;
    }
    public build_BExpression getBuild_bexpression() {
        return build_bexpression;
    }

    public void setBuild_bexpression(build_BExpression build_bexpression) {
        this.build_bexpression = build_bexpression;
    }

}