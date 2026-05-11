





import java.util.List;
import java.util.ArrayList;

public class build_context_IBuildContext  {






    private List<IAdvise> iadvises;




    private IResolver iresolver;




    private List<context_build_IBuildUnit> context_build_ibuildunits;


    public build_context_IBuildContext(
    ) {
        this.iadvises = new ArrayList<>();
        this.context_build_ibuildunits = new ArrayList<>();
    }

    public build_context_IBuildContext(
        ArrayList<IAdvise> iadvises,        ArrayList<context_build_IBuildUnit> context_build_ibuildunits    ) {
        this.iadvises = iadvises;
        this.context_build_ibuildunits = context_build_ibuildunits;
    }


    public List<IAdvise> getIadvises() {
        return iadvises;
    }

    public void addIadvise(Iadvise iadvise) {
        this.iadvises.add(iadvise);
    }
    public IResolver getIresolver() {
        return iresolver;
    }

    public void setIresolver(IResolver iresolver) {
        this.iresolver = iresolver;
    }
    public List<context_build_IBuildUnit> getContext_build_ibuildunits() {
        return context_build_ibuildunits;
    }

    public void addContext_build_ibuildunit(Context_build_ibuildunit context_build_ibuildunit) {
        this.context_build_ibuildunits.add(context_build_ibuildunit);
    }

}