





import java.util.List;
import java.util.ArrayList;

public class form_CSSCustomizable  {






    private List<form_EStringToStringMapEntry> form_estringtostringmapentrys;


    public form_CSSCustomizable(
    ) {
        this.form_estringtostringmapentrys = new ArrayList<>();
    }

    public form_CSSCustomizable(
        ArrayList<form_EStringToStringMapEntry> form_estringtostringmapentrys    ) {
        this.form_estringtostringmapentrys = form_estringtostringmapentrys;
    }


    public List<form_EStringToStringMapEntry> getForm_estringtostringmapentrys() {
        return form_estringtostringmapentrys;
    }

    public void addForm_estringtostringmapentry(Form_estringtostringmapentry form_estringtostringmapentry) {
        this.form_estringtostringmapentrys.add(form_estringtostringmapentry);
    }

}