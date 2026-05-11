





import java.util.List;
import java.util.ArrayList;

public class di_Style  {

    private String value;
    private String name;





    private di_View di_view;




    private di_DocumentRoot di_documentroot;


    public di_Style(
        String value,        String name    ) {
        this.value = value;
        this.name = name;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public di_View getDi_view() {
        return di_view;
    }

    public void setDi_view(di_View di_view) {
        this.di_view = di_view;
    }
    public di_DocumentRoot getDi_documentroot() {
        return di_documentroot;
    }

    public void setDi_documentroot(di_DocumentRoot di_documentroot) {
        this.di_documentroot = di_documentroot;
    }

}