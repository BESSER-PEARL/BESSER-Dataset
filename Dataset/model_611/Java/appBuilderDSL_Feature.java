





import java.util.List;
import java.util.ArrayList;

public class appBuilderDSL_Feature  {

    private boolean many;
    private String name;





    private appBuilderDSL_Type appbuilderdsl_type;




    private appBuilderDSL_Entity appbuilderdsl_entity;


    public appBuilderDSL_Feature(
        boolean many,        String name    ) {
        this.many = many;
        this.name = name;
    }


    public boolean getMany() {
        return many;
    }

    public void setMany(boolean many) {
        this.many = many;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public appBuilderDSL_Type getAppbuilderdsl_type() {
        return appbuilderdsl_type;
    }

    public void setAppbuilderdsl_type(appBuilderDSL_Type appbuilderdsl_type) {
        this.appbuilderdsl_type = appbuilderdsl_type;
    }
    public appBuilderDSL_Entity getAppbuilderdsl_entity() {
        return appbuilderdsl_entity;
    }

    public void setAppbuilderdsl_entity(appBuilderDSL_Entity appbuilderdsl_entity) {
        this.appbuilderdsl_entity = appbuilderdsl_entity;
    }

}