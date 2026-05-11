





import java.util.List;
import java.util.ArrayList;

public class applauseDsl_Entity extends Type {

    private boolean abstract;





    private applauseDsl_Entity applausedsl_entity;




    private applauseDsl_DataSource applausedsl_datasource;


    public applauseDsl_Entity(
        boolean abstract    ) {
        super(
        );
        this.abstract = abstract;
    }


    public boolean getAbstract() {
        return abstract;
    }

    public void setAbstract(boolean abstract) {
        this.abstract = abstract;
    }

    public applauseDsl_Entity getApplausedsl_entity() {
        return applausedsl_entity;
    }

    public void setApplausedsl_entity(applauseDsl_Entity applausedsl_entity) {
        this.applausedsl_entity = applausedsl_entity;
    }
    public applauseDsl_DataSource getApplausedsl_datasource() {
        return applausedsl_datasource;
    }

    public void setApplausedsl_datasource(applauseDsl_DataSource applausedsl_datasource) {
        this.applausedsl_datasource = applausedsl_datasource;
    }

}