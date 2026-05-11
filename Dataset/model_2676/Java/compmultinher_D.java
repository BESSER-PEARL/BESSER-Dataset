





import java.util.List;
import java.util.ArrayList;

public class compmultinher_D  {






    private List<compmultinher_E> compmultinher_es;


    public compmultinher_D(
    ) {
        this.compmultinher_es = new ArrayList<>();
    }

    public compmultinher_D(
        ArrayList<compmultinher_E> compmultinher_es    ) {
        this.compmultinher_es = compmultinher_es;
    }


    public List<compmultinher_E> getCompmultinher_es() {
        return compmultinher_es;
    }

    public void addCompmultinher_e(Compmultinher_e compmultinher_e) {
        this.compmultinher_es.add(compmultinher_e);
    }

}