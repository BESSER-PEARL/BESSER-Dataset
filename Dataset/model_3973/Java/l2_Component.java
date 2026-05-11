





import java.util.List;
import java.util.ArrayList;

public class l2_Component  {






    private l2_Subsystem l2_subsystem;




    private l2_Entity l2_entity;




    private l2_Process l2_process;




    private l2_Service l2_service;


    public l2_Component(
    ) {
    }



    public l2_Subsystem getL2_subsystem() {
        return l2_subsystem;
    }

    public void setL2_subsystem(l2_Subsystem l2_subsystem) {
        this.l2_subsystem = l2_subsystem;
    }
    public l2_Entity getL2_entity() {
        return l2_entity;
    }

    public void setL2_entity(l2_Entity l2_entity) {
        this.l2_entity = l2_entity;
    }
    public l2_Process getL2_process() {
        return l2_process;
    }

    public void setL2_process(l2_Process l2_process) {
        this.l2_process = l2_process;
    }
    public l2_Service getL2_service() {
        return l2_service;
    }

    public void setL2_service(l2_Service l2_service) {
        this.l2_service = l2_service;
    }

}