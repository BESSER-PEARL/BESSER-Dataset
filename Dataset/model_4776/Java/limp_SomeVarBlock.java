





import java.util.List;
import java.util.ArrayList;

public class limp_SomeVarBlock extends VarBlock {






    private List<limp_LocalArg> limp_localargs;


    public limp_SomeVarBlock(
    ) {
        super(
        );
        this.limp_localargs = new ArrayList<>();
    }

    public limp_SomeVarBlock(
        ArrayList<limp_LocalArg> limp_localargs    ) {
        this.limp_localargs = limp_localargs;
    }


    public List<limp_LocalArg> getLimp_localargs() {
        return limp_localargs;
    }

    public void addLimp_localarg(Limp_localarg limp_localarg) {
        this.limp_localargs.add(limp_localarg);
    }

}