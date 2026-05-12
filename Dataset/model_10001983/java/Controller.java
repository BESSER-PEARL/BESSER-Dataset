





import java.util.List;
import java.util.ArrayList;

public class Controller  {

    private String cars;
    private String floors;
    private String callQueue;
    private None callAdmin;





    private List<Floor> floors;




    private List<Call> calls;




    private List<Car> cars;


    public Controller(
        String cars,        String floors,        String callQueue,        None callAdmin    ) {
        this.cars = cars;
        this.floors = floors;
        this.callQueue = callQueue;
        this.callAdmin = callAdmin;
        this.floors = new ArrayList<>();
        this.calls = new ArrayList<>();
        this.cars = new ArrayList<>();
    }

    public Controller(
        String cars,        String floors,        String callQueue,        None callAdmin        ArrayList<Floor> floors,        ArrayList<Call> calls,        ArrayList<Car> cars    ) {
        this.cars = cars;
        this.floors = floors;
        this.callQueue = callQueue;
        this.callAdmin = callAdmin;
        this.floors = floors;
        this.calls = calls;
        this.cars = cars;
    }

    public String getCars() {
        return cars;
    }

    public void setCars(String cars) {
        this.cars = cars;
    }
    public String getFloors() {
        return floors;
    }

    public void setFloors(String floors) {
        this.floors = floors;
    }
    public String getCallqueue() {
        return callQueue;
    }

    public void setCallqueue(String callQueue) {
        this.callQueue = callQueue;
    }
    public None getCalladmin() {
        return callAdmin;
    }

    public void setCalladmin(None callAdmin) {
        this.callAdmin = callAdmin;
    }

    public List<Floor> getFloors() {
        return floors;
    }

    public void addFloor(Floor floor) {
        this.floors.add(floor);
    }
    public List<Call> getCalls() {
        return calls;
    }

    public void addCall(Call call) {
        this.calls.add(call);
    }
    public List<Car> getCars() {
        return cars;
    }

    public void addCar(Car car) {
        this.cars.add(car);
    }

}