





import java.util.List;
import java.util.ArrayList;

public class giraffeDSL_CloudType  {

    private String many;
    private String type;
    private String name;





    private giraffeDSL_CloudProvider giraffedsl_cloudprovider;


    public giraffeDSL_CloudType(
        String many,        String type,        String name    ) {
        this.many = many;
        this.type = type;
        this.name = name;
    }


    public String getMany() {
        return many;
    }

    public void setMany(String many) {
        this.many = many;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public giraffeDSL_CloudProvider getGiraffedsl_cloudprovider() {
        return giraffedsl_cloudprovider;
    }

    public void setGiraffedsl_cloudprovider(giraffeDSL_CloudProvider giraffedsl_cloudprovider) {
        this.giraffedsl_cloudprovider = giraffedsl_cloudprovider;
    }

}