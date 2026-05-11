





import java.util.List;
import java.util.ArrayList;

public class giraffeDSL_DeployAppSlaveMethodType  {

    private String many;
    private String name;
    private String type;





    private giraffeDSL_DeployApp giraffedsl_deployapp;


    public giraffeDSL_DeployAppSlaveMethodType(
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

    public giraffeDSL_DeployApp getGiraffedsl_deployapp() {
        return giraffedsl_deployapp;
    }

    public void setGiraffedsl_deployapp(giraffeDSL_DeployApp giraffedsl_deployapp) {
        this.giraffedsl_deployapp = giraffedsl_deployapp;
    }

}