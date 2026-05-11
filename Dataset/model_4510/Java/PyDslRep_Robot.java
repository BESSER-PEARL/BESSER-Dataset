





import java.util.List;
import java.util.ArrayList;

public class PyDslRep_Robot extends Entity {

    private String name;
    private int port;





    private PyDslRep_Environment pydslrep_environment;




    private List<PyDslRep_Wheel> pydslrep_wheels;




    private PyDslRep_MoveCollection pydslrep_movecollection;


    public PyDslRep_Robot(
        String name,        int port    ) {
        super(
        );
        this.name = name;
        this.port = port;
        this.pydslrep_wheels = new ArrayList<>();
    }

    public PyDslRep_Robot(
        String name,        int port        ArrayList<PyDslRep_Wheel> pydslrep_wheels    ) {
        this.name = name;
        this.port = port;
        this.pydslrep_wheels = pydslrep_wheels;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getPort() {
        return port;
    }

    public void setPort(int port) {
        this.port = port;
    }

    public PyDslRep_Environment getPydslrep_environment() {
        return pydslrep_environment;
    }

    public void setPydslrep_environment(PyDslRep_Environment pydslrep_environment) {
        this.pydslrep_environment = pydslrep_environment;
    }
    public List<PyDslRep_Wheel> getPydslrep_wheels() {
        return pydslrep_wheels;
    }

    public void addPydslrep_wheel(Pydslrep_wheel pydslrep_wheel) {
        this.pydslrep_wheels.add(pydslrep_wheel);
    }
    public PyDslRep_MoveCollection getPydslrep_movecollection() {
        return pydslrep_movecollection;
    }

    public void setPydslrep_movecollection(PyDslRep_MoveCollection pydslrep_movecollection) {
        this.pydslrep_movecollection = pydslrep_movecollection;
    }

}