





import java.util.List;
import java.util.ArrayList;

public class build_command_BuildUnitCommand  {






    private command_build_PropertyScope command_build_propertyscope;




    private IResolver iresolver;




    private List<IAdvise> iadvises;




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


    public command_build_PropertyScope getCommand_build_propertyscope() {
        return command_build_propertyscope;
    }

    public void setCommand_build_propertyscope(command_build_PropertyScope command_build_propertyscope) {
        this.command_build_propertyscope = command_build_propertyscope;
    }
    public IResolver getIresolver() {
        return iresolver;
    }

    public void setIresolver(IResolver iresolver) {
        this.iresolver = iresolver;
    }
    public List<IAdvise> getIadvises() {
        return iadvises;
    }

    public void addIadvise(Iadvise iadvise) {
        this.iadvises.add(iadvise);
    }
    public List<IUnitRequest> getIunitrequests() {
        return iunitrequests;
    }

    public void addIunitrequest(Iunitrequest iunitrequest) {
        this.iunitrequests.add(iunitrequest);
    }

}