





import java.util.List;
import java.util.ArrayList;

public class ric_FooterRegion  {






    private ric_Portal ric_portal;




    private List<ric_LineBreak> ric_linebreaks;




    private List<ric_BlockLevelComponent> ric_blocklevelcomponents;




    private List<ric_InlineComponent> ric_inlinecomponents;




    private List<ric_RichWidget> ric_richwidgets;




    private List<ric_ObjectComponent> ric_objectcomponents;


    public ric_FooterRegion(
    ) {
        this.ric_linebreaks = new ArrayList<>();
        this.ric_blocklevelcomponents = new ArrayList<>();
        this.ric_inlinecomponents = new ArrayList<>();
        this.ric_richwidgets = new ArrayList<>();
        this.ric_objectcomponents = new ArrayList<>();
    }

    public ric_FooterRegion(
        ArrayList<ric_LineBreak> ric_linebreaks,        ArrayList<ric_BlockLevelComponent> ric_blocklevelcomponents,        ArrayList<ric_InlineComponent> ric_inlinecomponents,        ArrayList<ric_RichWidget> ric_richwidgets,        ArrayList<ric_ObjectComponent> ric_objectcomponents    ) {
        this.ric_linebreaks = ric_linebreaks;
        this.ric_blocklevelcomponents = ric_blocklevelcomponents;
        this.ric_inlinecomponents = ric_inlinecomponents;
        this.ric_richwidgets = ric_richwidgets;
        this.ric_objectcomponents = ric_objectcomponents;
    }


    public ric_Portal getRic_portal() {
        return ric_portal;
    }

    public void setRic_portal(ric_Portal ric_portal) {
        this.ric_portal = ric_portal;
    }
    public List<ric_LineBreak> getRic_linebreaks() {
        return ric_linebreaks;
    }

    public void addRic_linebreak(Ric_linebreak ric_linebreak) {
        this.ric_linebreaks.add(ric_linebreak);
    }
    public List<ric_BlockLevelComponent> getRic_blocklevelcomponents() {
        return ric_blocklevelcomponents;
    }

    public void addRic_blocklevelcomponent(Ric_blocklevelcomponent ric_blocklevelcomponent) {
        this.ric_blocklevelcomponents.add(ric_blocklevelcomponent);
    }
    public List<ric_InlineComponent> getRic_inlinecomponents() {
        return ric_inlinecomponents;
    }

    public void addRic_inlinecomponent(Ric_inlinecomponent ric_inlinecomponent) {
        this.ric_inlinecomponents.add(ric_inlinecomponent);
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

}