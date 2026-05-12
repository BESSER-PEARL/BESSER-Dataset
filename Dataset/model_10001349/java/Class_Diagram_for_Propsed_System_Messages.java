





import java.util.List;
import java.util.ArrayList;

public class Class_Diagram_for_Propsed_System_Messages  {

    private String id;
    private int msg;
    private int sender;
    private String read_recipt;
    private int reciever;





    private Class_Diagram_for_Propsed_System_Employee class_diagram_for_propsed_system_employee;


    public Class_Diagram_for_Propsed_System_Messages(
        String id,        int msg,        int sender,        String read_recipt,        int reciever    ) {
        this.id = id;
        this.msg = msg;
        this.sender = sender;
        this.read_recipt = read_recipt;
        this.reciever = reciever;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public int getMsg() {
        return msg;
    }

    public void setMsg(int msg) {
        this.msg = msg;
    }
    public int getSender() {
        return sender;
    }

    public void setSender(int sender) {
        this.sender = sender;
    }
    public String getRead_recipt() {
        return read_recipt;
    }

    public void setRead_recipt(String read_recipt) {
        this.read_recipt = read_recipt;
    }
    public int getReciever() {
        return reciever;
    }

    public void setReciever(int reciever) {
        this.reciever = reciever;
    }

    public Class_Diagram_for_Propsed_System_Employee getClass_diagram_for_propsed_system_employee() {
        return class_diagram_for_propsed_system_employee;
    }

    public void setClass_diagram_for_propsed_system_employee(Class_Diagram_for_Propsed_System_Employee class_diagram_for_propsed_system_employee) {
        this.class_diagram_for_propsed_system_employee = class_diagram_for_propsed_system_employee;
    }

}