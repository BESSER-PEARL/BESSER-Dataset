





import java.util.List;
import java.util.ArrayList;

public class model_Activity extends BPELExtensibleElement {

    private String suppressJoinFailure;
    private String name;





    private model_Process model_process;




    private model_Else model_else;




    private model_Sources model_sources;




    private model_OnMessage model_onmessage;




    private model_ElseIf model_elseif;




    private model_CompensationHandler model_compensationhandler;




    private model_Targets model_targets;




    private model_OnEvent model_onevent;




    private model_TerminationHandler model_terminationhandler;




    private model_Source model_source;




    private model_Target model_target;




    private model_CatchAll model_catchall;




    private model_OnAlarm model_onalarm;


    public model_Activity(
        String suppressJoinFailure,        String name    ) {
        super(
        );
        this.suppressJoinFailure = suppressJoinFailure;
        this.name = name;
    }


    public String getSuppressjoinfailure() {
        return suppressJoinFailure;
    }

    public void setSuppressjoinfailure(String suppressJoinFailure) {
        this.suppressJoinFailure = suppressJoinFailure;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public model_Process getModel_process() {
        return model_process;
    }

    public void setModel_process(model_Process model_process) {
        this.model_process = model_process;
    }
    public model_Else getModel_else() {
        return model_else;
    }

    public void setModel_else(model_Else model_else) {
        this.model_else = model_else;
    }
    public model_Sources getModel_sources() {
        return model_sources;
    }

    public void setModel_sources(model_Sources model_sources) {
        this.model_sources = model_sources;
    }
    public model_OnMessage getModel_onmessage() {
        return model_onmessage;
    }

    public void setModel_onmessage(model_OnMessage model_onmessage) {
        this.model_onmessage = model_onmessage;
    }
    public model_ElseIf getModel_elseif() {
        return model_elseif;
    }

    public void setModel_elseif(model_ElseIf model_elseif) {
        this.model_elseif = model_elseif;
    }
    public model_CompensationHandler getModel_compensationhandler() {
        return model_compensationhandler;
    }

    public void setModel_compensationhandler(model_CompensationHandler model_compensationhandler) {
        this.model_compensationhandler = model_compensationhandler;
    }
    public model_Targets getModel_targets() {
        return model_targets;
    }

    public void setModel_targets(model_Targets model_targets) {
        this.model_targets = model_targets;
    }
    public model_OnEvent getModel_onevent() {
        return model_onevent;
    }

    public void setModel_onevent(model_OnEvent model_onevent) {
        this.model_onevent = model_onevent;
    }
    public model_TerminationHandler getModel_terminationhandler() {
        return model_terminationhandler;
    }

    public void setModel_terminationhandler(model_TerminationHandler model_terminationhandler) {
        this.model_terminationhandler = model_terminationhandler;
    }
    public model_Source getModel_source() {
        return model_source;
    }

    public void setModel_source(model_Source model_source) {
        this.model_source = model_source;
    }
    public model_Target getModel_target() {
        return model_target;
    }

    public void setModel_target(model_Target model_target) {
        this.model_target = model_target;
    }
    public model_CatchAll getModel_catchall() {
        return model_catchall;
    }

    public void setModel_catchall(model_CatchAll model_catchall) {
        this.model_catchall = model_catchall;
    }
    public model_OnAlarm getModel_onalarm() {
        return model_onalarm;
    }

    public void setModel_onalarm(model_OnAlarm model_onalarm) {
        this.model_onalarm = model_onalarm;
    }

}