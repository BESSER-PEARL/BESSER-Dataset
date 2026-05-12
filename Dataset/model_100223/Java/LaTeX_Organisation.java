





import java.util.List;
import java.util.ArrayList;

public class LaTeX_Organisation  {






    private List<Name> names;


    public LaTeX_Organisation(
    ) {
        this.names = new ArrayList<>();
    }

    public LaTeX_Organisation(
        ArrayList<Name> names    ) {
        this.names = names;
    }


    public List<Name> getNames() {
        return names;
    }

    public void addName(Name name) {
        this.names.add(name);
    }

}