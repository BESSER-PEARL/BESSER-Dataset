





import java.util.List;
import java.util.ArrayList;

public class typeB_BlockB  {






    private List<typeB_OutPortB> typeb_outportbs;


    public typeB_BlockB(
    ) {
        this.typeb_outportbs = new ArrayList<>();
    }

    public typeB_BlockB(
        ArrayList<typeB_OutPortB> typeb_outportbs    ) {
        this.typeb_outportbs = typeb_outportbs;
    }


    public List<typeB_OutPortB> getTypeb_outportbs() {
        return typeb_outportbs;
    }

    public void addTypeb_outportb(Typeb_outportb typeb_outportb) {
        this.typeb_outportbs.add(typeb_outportb);
    }

}