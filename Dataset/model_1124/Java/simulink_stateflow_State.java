





import java.util.List;
import java.util.ArrayList;

public class simulink_stateflow_State extends Node {

    private int priority;
    private String name;
    private String subStateType;
    private boolean initial;





    private List<Data> datas;




    private List<Data> datas;


    public simulink_stateflow_State(
        int priority,        String name,        String subStateType,        boolean initial    ) {
        super(
        );
        this.priority = priority;
        this.name = name;
        this.subStateType = subStateType;
        this.initial = initial;
        this.datas = new ArrayList<>();
        this.datas = new ArrayList<>();
    }

    public simulink_stateflow_State(
        int priority,        String name,        String subStateType,        boolean initial        ArrayList<Data> datas,        ArrayList<Data> datas    ) {
        this.priority = priority;
        this.name = name;
        this.subStateType = subStateType;
        this.initial = initial;
        this.datas = datas;
        this.datas = datas;
    }

    public int getPriority() {
        return priority;
    }

    public void setPriority(int priority) {
        this.priority = priority;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getSubstatetype() {
        return subStateType;
    }

    public void setSubstatetype(String subStateType) {
        this.subStateType = subStateType;
    }
    public boolean getInitial() {
        return initial;
    }

    public void setInitial(boolean initial) {
        this.initial = initial;
    }

    public List<Data> getDatas() {
        return datas;
    }

    public void addData(Data data) {
        this.datas.add(data);
    }
    public List<Data> getDatas() {
        return datas;
    }

    public void addData(Data data) {
        this.datas.add(data);
    }

}