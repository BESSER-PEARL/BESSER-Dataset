





import java.util.List;
import java.util.ArrayList;

public class Class_Diagram_for_Propsed_System_Messages  {

    private int sender;
    private int id;
    private int reciever;
    private String message;
    private String read_recipt;





    private Class_Diagram_for_Propsed_System_Employee class_diagram_for_propsed_system_employee;


    public Class_Diagram_for_Propsed_System_Messages(
        int sender,        int id,        int reciever,        String message,        String read_recipt    ) {
        this.sender = sender;
        this.id = id;
        this.reciever = reciever;
        this.message = message;
        this.read_recipt = read_recipt;
    }


    public int getSender() {
        return sender;
    }

    public void setSender(int sender) {
        this.sender = sender;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public int getReciever() {
        return reciever;
    }

    public void setReciever(int reciever) {
        this.reciever = reciever;
    }
    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
    public String getRead_recipt() {
        return read_recipt;
    }

    public void setRead_recipt(String read_recipt) {
        this.read_recipt = read_recipt;
    }

    public Class_Diagram_for_Propsed_System_Employee getClass_diagram_for_propsed_system_employee() {
        return class_diagram_for_propsed_system_employee;
    }

    public void setClass_diagram_for_propsed_system_employee(Class_Diagram_for_Propsed_System_Employee class_diagram_for_propsed_system_employee) {
        this.class_diagram_for_propsed_system_employee = class_diagram_for_propsed_system_employee;
    }

}