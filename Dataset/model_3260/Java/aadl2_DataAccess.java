





import java.util.List;
import java.util.ArrayList;

public class aadl2_DataAccess extends ParameterConnectionEnd, FlowElement, Access, PortConnectionEnd {






    private aadl2_SystemType aadl2_systemtype;




    private aadl2_DataClassifier aadl2_dataclassifier;




    private aadl2_ThreadType aadl2_threadtype;




    private aadl2_ThreadGroupType aadl2_threadgrouptype;




    private aadl2_SubprogramType aadl2_subprogramtype;




    private aadl2_ProcessType aadl2_processtype;


    public aadl2_DataAccess(
    ) {
        super(
        );
    }



    public aadl2_SystemType getAadl2_systemtype() {
        return aadl2_systemtype;
    }

    public void setAadl2_systemtype(aadl2_SystemType aadl2_systemtype) {
        this.aadl2_systemtype = aadl2_systemtype;
    }
    public aadl2_DataClassifier getAadl2_dataclassifier() {
        return aadl2_dataclassifier;
    }

    public void setAadl2_dataclassifier(aadl2_DataClassifier aadl2_dataclassifier) {
        this.aadl2_dataclassifier = aadl2_dataclassifier;
    }
    public aadl2_ThreadType getAadl2_threadtype() {
        return aadl2_threadtype;
    }

    public void setAadl2_threadtype(aadl2_ThreadType aadl2_threadtype) {
        this.aadl2_threadtype = aadl2_threadtype;
    }
    public aadl2_ThreadGroupType getAadl2_threadgrouptype() {
        return aadl2_threadgrouptype;
    }

    public void setAadl2_threadgrouptype(aadl2_ThreadGroupType aadl2_threadgrouptype) {
        this.aadl2_threadgrouptype = aadl2_threadgrouptype;
    }
    public aadl2_SubprogramType getAadl2_subprogramtype() {
        return aadl2_subprogramtype;
    }

    public void setAadl2_subprogramtype(aadl2_SubprogramType aadl2_subprogramtype) {
        this.aadl2_subprogramtype = aadl2_subprogramtype;
    }
    public aadl2_ProcessType getAadl2_processtype() {
        return aadl2_processtype;
    }

    public void setAadl2_processtype(aadl2_ProcessType aadl2_processtype) {
        this.aadl2_processtype = aadl2_processtype;
    }

}