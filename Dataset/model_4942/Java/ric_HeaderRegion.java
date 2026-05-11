





import java.util.List;
import java.util.ArrayList;

public class ric_HeaderRegion  {






    private List<ric_LineBreak> ric_linebreaks;




    private ric_Portal ric_portal;




    private List<ric_InlineComponent> ric_inlinecomponents;


    public ric_HeaderRegion(
    ) {
        this.ric_linebreaks = new ArrayList<>();
        this.ric_inlinecomponents = new ArrayList<>();
    }

    public ric_HeaderRegion(
        ArrayList<ric_LineBreak> ric_linebreaks,        ArrayList<ric_InlineComponent> ric_inlinecomponents    ) {
        this.ric_linebreaks = ric_linebreaks;
        this.ric_inlinecomponents = ric_inlinecomponents;
    }


    public List<ric_LineBreak> getRic_linebreaks() {
        return ric_linebreaks;
    }

    public void addRic_linebreak(Ric_linebreak ric_linebreak) {
        this.ric_linebreaks.add(ric_linebreak);
    }
    public ric_Portal getRic_portal() {
        return ric_portal;
    }

    public void setRic_portal(ric_Portal ric_portal) {
        this.ric_portal = ric_portal;
    }
    public List<ric_InlineComponent> getRic_inlinecomponents() {
        return ric_inlinecomponents;
    }

    public void addRic_inlinecomponent(Ric_inlinecomponent ric_inlinecomponent) {
        this.ric_inlinecomponents.add(ric_inlinecomponent);
    }

}