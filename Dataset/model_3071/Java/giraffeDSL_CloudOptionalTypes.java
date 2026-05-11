





import java.util.List;
import java.util.ArrayList;

public class giraffeDSL_CloudOptionalTypes  {

    private String many;
    private String name;
    private String type;





    private giraffeDSL_CloudProvider giraffedsl_cloudprovider;


    public giraffeDSL_CloudOptionalTypes(
        String many,        String name,        String type    ) {
        this.many = many;
        this.name = name;
        this.type = type;
    }


    public String getMany() {
        return many;
    }

    public void setMany(String many) {
        this.many = many;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public giraffeDSL_CloudProvider getGiraffedsl_cloudprovider() {
        return giraffedsl_cloudprovider;
    }

    public void setGiraffedsl_cloudprovider(giraffeDSL_CloudProvider giraffedsl_cloudprovider) {
        this.giraffedsl_cloudprovider = giraffedsl_cloudprovider;
    }

}