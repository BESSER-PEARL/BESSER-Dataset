





import java.util.List;
import java.util.ArrayList;

public class domainDsl_Feature  {

    private String name;
    private String defaultVal;
    private boolean many;





    private domainDsl_Type domaindsl_type;




    private domainDsl_Entity domaindsl_entity;


    public domainDsl_Feature(
        String name,        String defaultVal,        boolean many    ) {
        this.name = name;
        this.defaultVal = defaultVal;
        this.many = many;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDefaultval() {
        return defaultVal;
    }

    public void setDefaultval(String defaultVal) {
        this.defaultVal = defaultVal;
    }
    public boolean getMany() {
        return many;
    }

    public void setMany(boolean many) {
        this.many = many;
    }

    public domainDsl_Type getDomaindsl_type() {
        return domaindsl_type;
    }

    public void setDomaindsl_type(domainDsl_Type domaindsl_type) {
        this.domaindsl_type = domaindsl_type;
    }
    public domainDsl_Entity getDomaindsl_entity() {
        return domaindsl_entity;
    }

    public void setDomaindsl_entity(domainDsl_Entity domaindsl_entity) {
        this.domaindsl_entity = domaindsl_entity;
    }

}