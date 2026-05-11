





import java.util.List;
import java.util.ArrayList;

public class giraffeDSL_DeployAppFeature  {

    private String name;
    private String many;





    private giraffeDSL_Deploy giraffedsl_deploy;




    private giraffeDSL_DeployApp giraffedsl_deployapp;


    public giraffeDSL_DeployAppFeature(
        String name,        String many    ) {
        this.name = name;
        this.many = many;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getMany() {
        return many;
    }

    public void setMany(String many) {
        this.many = many;
    }

    public giraffeDSL_Deploy getGiraffedsl_deploy() {
        return giraffedsl_deploy;
    }

    public void setGiraffedsl_deploy(giraffeDSL_Deploy giraffedsl_deploy) {
        this.giraffedsl_deploy = giraffedsl_deploy;
    }
    public giraffeDSL_DeployApp getGiraffedsl_deployapp() {
        return giraffedsl_deployapp;
    }

    public void setGiraffedsl_deployapp(giraffeDSL_DeployApp giraffedsl_deployapp) {
        this.giraffedsl_deployapp = giraffedsl_deployapp;
    }

}