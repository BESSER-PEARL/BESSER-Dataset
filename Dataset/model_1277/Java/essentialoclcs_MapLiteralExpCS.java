





import java.util.List;
import java.util.ArrayList;

public class essentialoclcs_MapLiteralExpCS extends LiteralExpCS {






    private essentialoclcs_MapTypeCS essentialoclcs_maptypecs;




    private List<essentialoclcs_MapLiteralPartCS> essentialoclcs_mapliteralpartcss;


    public essentialoclcs_MapLiteralExpCS(
    ) {
        super(
        );
        this.essentialoclcs_mapliteralpartcss = new ArrayList<>();
    }

    public essentialoclcs_MapLiteralExpCS(
        ArrayList<essentialoclcs_MapLiteralPartCS> essentialoclcs_mapliteralpartcss    ) {
        this.essentialoclcs_mapliteralpartcss = essentialoclcs_mapliteralpartcss;
    }


    public essentialoclcs_MapTypeCS getEssentialoclcs_maptypecs() {
        return essentialoclcs_maptypecs;
    }

    public void setEssentialoclcs_maptypecs(essentialoclcs_MapTypeCS essentialoclcs_maptypecs) {
        this.essentialoclcs_maptypecs = essentialoclcs_maptypecs;
    }
    public List<essentialoclcs_MapLiteralPartCS> getEssentialoclcs_mapliteralpartcss() {
        return essentialoclcs_mapliteralpartcss;
    }

    public void addEssentialoclcs_mapliteralpartcs(Essentialoclcs_mapliteralpartcs essentialoclcs_mapliteralpartcs) {
        this.essentialoclcs_mapliteralpartcss.add(essentialoclcs_mapliteralpartcs);
    }

}