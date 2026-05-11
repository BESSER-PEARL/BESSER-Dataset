





import java.util.List;
import java.util.ArrayList;

public class compmultinher_F  {






    private List<compmultinher_H> compmultinher_hs;




    private List<compmultinher_G> compmultinher_gs;


    public compmultinher_F(
    ) {
        this.compmultinher_hs = new ArrayList<>();
        this.compmultinher_gs = new ArrayList<>();
    }

    public compmultinher_F(
        ArrayList<compmultinher_H> compmultinher_hs,        ArrayList<compmultinher_G> compmultinher_gs    ) {
        this.compmultinher_hs = compmultinher_hs;
        this.compmultinher_gs = compmultinher_gs;
    }


    public List<compmultinher_H> getCompmultinher_hs() {
        return compmultinher_hs;
    }

    public void addCompmultinher_h(Compmultinher_h compmultinher_h) {
        this.compmultinher_hs.add(compmultinher_h);
    }
    public List<compmultinher_G> getCompmultinher_gs() {
        return compmultinher_gs;
    }

    public void addCompmultinher_g(Compmultinher_g compmultinher_g) {
        this.compmultinher_gs.add(compmultinher_g);
    }

}