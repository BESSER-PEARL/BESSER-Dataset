





import java.util.List;
import java.util.ArrayList;

public class opposite2_AbstractClassB  {






    private opposite2_Root opposite2_root;




    private opposite2_EndA opposite2_enda;




    private List<opposite2_EndA> opposite2_endas;


    public opposite2_AbstractClassB(
    ) {
        this.opposite2_endas = new ArrayList<>();
    }

    public opposite2_AbstractClassB(
        ArrayList<opposite2_EndA> opposite2_endas    ) {
        this.opposite2_endas = opposite2_endas;
    }


    public opposite2_Root getOpposite2_root() {
        return opposite2_root;
    }

    public void setOpposite2_root(opposite2_Root opposite2_root) {
        this.opposite2_root = opposite2_root;
    }
    public opposite2_EndA getOpposite2_enda() {
        return opposite2_enda;
    }

    public void setOpposite2_enda(opposite2_EndA opposite2_enda) {
        this.opposite2_enda = opposite2_enda;
    }
    public List<opposite2_EndA> getOpposite2_endas() {
        return opposite2_endas;
    }

    public void addOpposite2_enda(Opposite2_enda opposite2_enda) {
        this.opposite2_endas.add(opposite2_enda);
    }

}