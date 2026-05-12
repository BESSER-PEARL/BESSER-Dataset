





import java.util.List;
import java.util.ArrayList;

public class Styling_Styling  {






    private List<Styling_StylingModel> styling_stylingmodels;


    public Styling_Styling(
    ) {
        this.styling_stylingmodels = new ArrayList<>();
    }

    public Styling_Styling(
        ArrayList<Styling_StylingModel> styling_stylingmodels    ) {
        this.styling_stylingmodels = styling_stylingmodels;
    }


    public List<Styling_StylingModel> getStyling_stylingmodels() {
        return styling_stylingmodels;
    }

    public void addStyling_stylingmodel(Styling_stylingmodel styling_stylingmodel) {
        this.styling_stylingmodels.add(styling_stylingmodel);
    }

}