





import java.util.List;
import java.util.ArrayList;

public class fml_SelectionItem  {

    private boolean selected;
    private String Text;
    private boolean preselected;





    private fml_SelectField fml_selectfield;




    private fml_SelectField fml_selectfield;




    private List<fml_PageElement> fml_pageelements;




    private fml_PageElement fml_pageelement;


    public fml_SelectionItem(
        boolean selected,        String Text,        boolean preselected    ) {
        this.selected = selected;
        this.Text = Text;
        this.preselected = preselected;
        this.fml_pageelements = new ArrayList<>();
    }

    public fml_SelectionItem(
        boolean selected,        String Text,        boolean preselected        ArrayList<fml_PageElement> fml_pageelements    ) {
        this.selected = selected;
        this.Text = Text;
        this.preselected = preselected;
        this.fml_pageelements = fml_pageelements;
    }

    public boolean getSelected() {
        return selected;
    }

    public void setSelected(boolean selected) {
        this.selected = selected;
    }
    public String getText() {
        return Text;
    }

    public void setText(String Text) {
        this.Text = Text;
    }
    public boolean getPreselected() {
        return preselected;
    }

    public void setPreselected(boolean preselected) {
        this.preselected = preselected;
    }

    public fml_SelectField getFml_selectfield() {
        return fml_selectfield;
    }

    public void setFml_selectfield(fml_SelectField fml_selectfield) {
        this.fml_selectfield = fml_selectfield;
    }
    public fml_SelectField getFml_selectfield() {
        return fml_selectfield;
    }

    public void setFml_selectfield(fml_SelectField fml_selectfield) {
        this.fml_selectfield = fml_selectfield;
    }
    public List<fml_PageElement> getFml_pageelements() {
        return fml_pageelements;
    }

    public void addFml_pageelement(Fml_pageelement fml_pageelement) {
        this.fml_pageelements.add(fml_pageelement);
    }
    public fml_PageElement getFml_pageelement() {
        return fml_pageelement;
    }

    public void setFml_pageelement(fml_PageElement fml_pageelement) {
        this.fml_pageelement = fml_pageelement;
    }

}