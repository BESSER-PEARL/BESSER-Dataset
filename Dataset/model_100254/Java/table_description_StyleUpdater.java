





import java.util.List;
import java.util.ArrayList;

public class table_description_StyleUpdater  {






    private List<BackgroundConditionalStyle> backgroundconditionalstyles;




    private BackgroundStyleDescription backgroundstyledescription;


    public table_description_StyleUpdater(
    ) {
        this.backgroundconditionalstyles = new ArrayList<>();
    }

    public table_description_StyleUpdater(
        ArrayList<BackgroundConditionalStyle> backgroundconditionalstyles    ) {
        this.backgroundconditionalstyles = backgroundconditionalstyles;
    }


    public List<BackgroundConditionalStyle> getBackgroundconditionalstyles() {
        return backgroundconditionalstyles;
    }

    public void addBackgroundconditionalstyle(Backgroundconditionalstyle backgroundconditionalstyle) {
        this.backgroundconditionalstyles.add(backgroundconditionalstyle);
    }
    public BackgroundStyleDescription getBackgroundstyledescription() {
        return backgroundstyledescription;
    }

    public void setBackgroundstyledescription(BackgroundStyleDescription backgroundstyledescription) {
        this.backgroundstyledescription = backgroundstyledescription;
    }

}