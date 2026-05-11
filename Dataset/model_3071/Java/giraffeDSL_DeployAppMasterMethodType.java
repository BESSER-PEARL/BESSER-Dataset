





import java.util.List;
import java.util.ArrayList;

public class giraffeDSL_DeployAppMasterMethodType  {

    private String many;
    private String type;
    private String name;





    private giraffeDSL_DeployApp giraffedsl_deployapp;


    public giraffeDSL_DeployAppMasterMethodType(
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

    public giraffeDSL_DeployApp getGiraffedsl_deployapp() {
        return giraffedsl_deployapp;
    }

    public void setGiraffedsl_deployapp(giraffeDSL_DeployApp giraffedsl_deployapp) {
        this.giraffedsl_deployapp = giraffedsl_deployapp;
    }

}