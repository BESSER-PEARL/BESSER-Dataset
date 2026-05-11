





import java.util.List;
import java.util.ArrayList;

public class cgimodel_BaseState  {

    private String name;





    private cgimodel_StateModel cgimodel_statemodel;




    private cgimodel_OrState cgimodel_orstate;


    public cgimodel_BaseState(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public cgimodel_StateModel getCgimodel_statemodel() {
        return cgimodel_statemodel;
    }

    public void setCgimodel_statemodel(cgimodel_StateModel cgimodel_statemodel) {
        this.cgimodel_statemodel = cgimodel_statemodel;
    }
    public cgimodel_OrState getCgimodel_orstate() {
        return cgimodel_orstate;
    }

    public void setCgimodel_orstate(cgimodel_OrState cgimodel_orstate) {
        this.cgimodel_orstate = cgimodel_orstate;
    }

}