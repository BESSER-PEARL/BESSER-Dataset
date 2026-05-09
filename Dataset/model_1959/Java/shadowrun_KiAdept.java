





import java.util.List;
import java.util.ArrayList;

public class shadowrun_KiAdept extends AbstractMagischePaersona {






    private shadowrun_KiKraft shadowrun_kikraft;




    private List<shadowrun_KiKraft> shadowrun_kikrafts;


    public shadowrun_KiAdept(
    ) {
        super(
        );
        this.shadowrun_kikrafts = new ArrayList<>();
    }

    public shadowrun_KiAdept(
        ArrayList<shadowrun_KiKraft> shadowrun_kikrafts    ) {
        this.shadowrun_kikrafts = shadowrun_kikrafts;
    }


    public shadowrun_KiKraft getShadowrun_kikraft() {
        return shadowrun_kikraft;
    }

    public void setShadowrun_kikraft(shadowrun_KiKraft shadowrun_kikraft) {
        this.shadowrun_kikraft = shadowrun_kikraft;
    }
    public List<shadowrun_KiKraft> getShadowrun_kikrafts() {
        return shadowrun_kikrafts;
    }

    public void addShadowrun_kikraft(Shadowrun_kikraft shadowrun_kikraft) {
        this.shadowrun_kikrafts.add(shadowrun_kikraft);
    }

}