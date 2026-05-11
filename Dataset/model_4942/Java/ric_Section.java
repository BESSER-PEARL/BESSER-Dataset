





import java.util.List;
import java.util.ArrayList;

public class ric_Section  {

    private String title;





    private List<ric_InlineComponent> ric_inlinecomponents;




    private ric_AccordionPanel ric_accordionpanel;




    private List<ric_BlockLevelComponent> ric_blocklevelcomponents;




    private List<ric_List> ric_lists;




    private List<ric_RichWidget> ric_richwidgets;




    private List<ric_ObjectComponent> ric_objectcomponents;




    private List<ric_Form> ric_forms;




    private List<ric_LineBreak> ric_linebreaks;


    public ric_Section(
        String title    ) {
        this.title = title;
        this.ric_inlinecomponents = new ArrayList<>();
        this.ric_blocklevelcomponents = new ArrayList<>();
        this.ric_lists = new ArrayList<>();
        this.ric_richwidgets = new ArrayList<>();
        this.ric_objectcomponents = new ArrayList<>();
        this.ric_forms = new ArrayList<>();
        this.ric_linebreaks = new ArrayList<>();
    }

    public ric_Section(
        String title        ArrayList<ric_InlineComponent> ric_inlinecomponents,        ArrayList<ric_BlockLevelComponent> ric_blocklevelcomponents,        ArrayList<ric_List> ric_lists,        ArrayList<ric_RichWidget> ric_richwidgets,        ArrayList<ric_ObjectComponent> ric_objectcomponents,        ArrayList<ric_Form> ric_forms,        ArrayList<ric_LineBreak> ric_linebreaks    ) {
        this.title = title;
        this.ric_inlinecomponents = ric_inlinecomponents;
        this.ric_blocklevelcomponents = ric_blocklevelcomponents;
        this.ric_lists = ric_lists;
        this.ric_richwidgets = ric_richwidgets;
        this.ric_objectcomponents = ric_objectcomponents;
        this.ric_forms = ric_forms;
        this.ric_linebreaks = ric_linebreaks;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public List<ric_InlineComponent> getRic_inlinecomponents() {
        return ric_inlinecomponents;
    }

    public void addRic_inlinecomponent(Ric_inlinecomponent ric_inlinecomponent) {
        this.ric_inlinecomponents.add(ric_inlinecomponent);
    }
    public ric_AccordionPanel getRic_accordionpanel() {
        return ric_accordionpanel;
    }

    public void setRic_accordionpanel(ric_AccordionPanel ric_accordionpanel) {
        this.ric_accordionpanel = ric_accordionpanel;
    }
    public List<ric_BlockLevelComponent> getRic_blocklevelcomponents() {
        return ric_blocklevelcomponents;
    }

    public void addRic_blocklevelcomponent(Ric_blocklevelcomponent ric_blocklevelcomponent) {
        this.ric_blocklevelcomponents.add(ric_blocklevelcomponent);
    }
    public List<ric_List> getRic_lists() {
        return ric_lists;
    }

    public void addRic_list(Ric_list ric_list) {
        this.ric_lists.add(ric_list);
    }
    public List<ric_RichWidget> getRic_richwidgets() {
        return ric_richwidgets;
    }

    public void addRic_richwidget(Ric_richwidget ric_richwidget) {
        this.ric_richwidgets.add(ric_richwidget);
    }
    public List<ric_ObjectComponent> getRic_objectcomponents() {
        return ric_objectcomponents;
    }

    public void addRic_objectcomponent(Ric_objectcomponent ric_objectcomponent) {
        this.ric_objectcomponents.add(ric_objectcomponent);
    }
    public List<ric_Form> getRic_forms() {
        return ric_forms;
    }

    public void addRic_form(Ric_form ric_form) {
        this.ric_forms.add(ric_form);
    }
    public List<ric_LineBreak> getRic_linebreaks() {
        return ric_linebreaks;
    }

    public void addRic_linebreak(Ric_linebreak ric_linebreak) {
        this.ric_linebreaks.add(ric_linebreak);
    }

}