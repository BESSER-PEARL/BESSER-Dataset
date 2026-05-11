





import java.util.List;
import java.util.ArrayList;

public class dsl_Action  {






    private dsl_Resource dsl_resource;




    private dsl_ElseDoSpec dsl_elsedospec;




    private dsl_State dsl_state;




    private dsl_ElseIfDoSpec dsl_elseifdospec;




    private dsl_IfDoSpec dsl_ifdospec;


    public dsl_Action(
    ) {
    }



    public dsl_Resource getDsl_resource() {
        return dsl_resource;
    }

    public void setDsl_resource(dsl_Resource dsl_resource) {
        this.dsl_resource = dsl_resource;
    }
    public dsl_ElseDoSpec getDsl_elsedospec() {
        return dsl_elsedospec;
    }

    public void setDsl_elsedospec(dsl_ElseDoSpec dsl_elsedospec) {
        this.dsl_elsedospec = dsl_elsedospec;
    }
    public dsl_State getDsl_state() {
        return dsl_state;
    }

    public void setDsl_state(dsl_State dsl_state) {
        this.dsl_state = dsl_state;
    }
    public dsl_ElseIfDoSpec getDsl_elseifdospec() {
        return dsl_elseifdospec;
    }

    public void setDsl_elseifdospec(dsl_ElseIfDoSpec dsl_elseifdospec) {
        this.dsl_elseifdospec = dsl_elseifdospec;
    }
    public dsl_IfDoSpec getDsl_ifdospec() {
        return dsl_ifdospec;
    }

    public void setDsl_ifdospec(dsl_IfDoSpec dsl_ifdospec) {
        this.dsl_ifdospec = dsl_ifdospec;
    }

}