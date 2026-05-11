





import java.util.List;
import java.util.ArrayList;

public class viewpoint_diagram_ComputedStyleDescriptionRegistry  {






    private List<style_StyleDescription> style_styledescriptions;


    public viewpoint_diagram_ComputedStyleDescriptionRegistry(
    ) {
        this.style_styledescriptions = new ArrayList<>();
    }

    public viewpoint_diagram_ComputedStyleDescriptionRegistry(
        ArrayList<style_StyleDescription> style_styledescriptions    ) {
        this.style_styledescriptions = style_styledescriptions;
    }


    public List<style_StyleDescription> getStyle_styledescriptions() {
        return style_styledescriptions;
    }

    public void addStyle_styledescription(Style_styledescription style_styledescription) {
        this.style_styledescriptions.add(style_styledescription);
    }

}