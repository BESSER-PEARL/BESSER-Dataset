





import java.util.List;
import java.util.ArrayList;

public class IDataNodeFunction  {






    private actions_SetDataAction actions_setdataaction;




    private actions_GetDataAction actions_getdataaction;


    public IDataNodeFunction(
    ) {
    }



    public actions_SetDataAction getActions_setdataaction() {
        return actions_setdataaction;
    }

    public void setActions_setdataaction(actions_SetDataAction actions_setdataaction) {
        this.actions_setdataaction = actions_setdataaction;
    }
    public actions_GetDataAction getActions_getdataaction() {
        return actions_getdataaction;
    }

    public void setActions_getdataaction(actions_GetDataAction actions_getdataaction) {
        this.actions_getdataaction = actions_getdataaction;
    }

}