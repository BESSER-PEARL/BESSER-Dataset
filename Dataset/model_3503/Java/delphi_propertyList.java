





import java.util.List;
import java.util.ArrayList;

public class delphi_propertyList extends CSTrace {

    private String port;





    private delphi_ident delphi_ident;




    private delphi_classProperty delphi_classproperty;




    private delphi_propertyInterface delphi_propertyinterface;




    private delphi_propertySpecifiers delphi_propertyspecifiers;


    public delphi_propertyList(
        String port    ) {
        super(
        );
        this.port = port;
    }


    public String getPort() {
        return port;
    }

    public void setPort(String port) {
        this.port = port;
    }

    public delphi_ident getDelphi_ident() {
        return delphi_ident;
    }

    public void setDelphi_ident(delphi_ident delphi_ident) {
        this.delphi_ident = delphi_ident;
    }
    public delphi_classProperty getDelphi_classproperty() {
        return delphi_classproperty;
    }

    public void setDelphi_classproperty(delphi_classProperty delphi_classproperty) {
        this.delphi_classproperty = delphi_classproperty;
    }
    public delphi_propertyInterface getDelphi_propertyinterface() {
        return delphi_propertyinterface;
    }

    public void setDelphi_propertyinterface(delphi_propertyInterface delphi_propertyinterface) {
        this.delphi_propertyinterface = delphi_propertyinterface;
    }
    public delphi_propertySpecifiers getDelphi_propertyspecifiers() {
        return delphi_propertyspecifiers;
    }

    public void setDelphi_propertyspecifiers(delphi_propertySpecifiers delphi_propertyspecifiers) {
        this.delphi_propertyspecifiers = delphi_propertyspecifiers;
    }

}