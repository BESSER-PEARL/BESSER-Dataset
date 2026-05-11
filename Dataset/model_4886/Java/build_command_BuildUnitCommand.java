





import java.util.List;
import java.util.ArrayList;

public class build_command_BuildUnitCommand  {






    private List<IAdvise> iadvises;




    private IResolver iresolver;




    private List<IUnitRequest> iunitrequests;


    public build_command_BuildUnitCommand(
    ) {
        this.iadvises = new ArrayList<>();
        this.iunitrequests = new ArrayList<>();
    }

    public build_command_BuildUnitCommand(
        ArrayList<IAdvise> iadvises,        ArrayList<IUnitRequest> iunitrequests    ) {
        this.iadvises = iadvises;
        this.iunitrequests = iunitrequests;
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
    public List<IUnitRequest> getIunitrequests() {
        return iunitrequests;
    }

    public void addIunitrequest(Iunitrequest iunitrequest) {
        this.iunitrequests.add(iunitrequest);
    }

}