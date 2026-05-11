





import java.util.List;
import java.util.ArrayList;

public class di_ElementEntry  {

    private String value;





    private di_View di_view;




    private di_Guide di_guide;


    public di_ElementEntry(
        String value    ) {
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public di_View getDi_view() {
        return di_view;
    }

    public void setDi_view(di_View di_view) {
        this.di_view = di_view;
    }
    public di_Guide getDi_guide() {
        return di_guide;
    }

    public void setDi_guide(di_Guide di_guide) {
        this.di_guide = di_guide;
    }

}