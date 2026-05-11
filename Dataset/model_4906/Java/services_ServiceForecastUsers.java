





import java.util.List;
import java.util.ArrayList;

public class services_ServiceForecastUsers  {






    private services_ServiceForecast services_serviceforecast;




    private List<services_Value> services_values;




    private services_ServiceUser services_serviceuser;


    public services_ServiceForecastUsers(
    ) {
        this.services_values = new ArrayList<>();
    }

    public services_ServiceForecastUsers(
        ArrayList<services_Value> services_values    ) {
        this.services_values = services_values;
    }


    public services_ServiceForecast getServices_serviceforecast() {
        return services_serviceforecast;
    }

    public void setServices_serviceforecast(services_ServiceForecast services_serviceforecast) {
        this.services_serviceforecast = services_serviceforecast;
    }
    public List<services_Value> getServices_values() {
        return services_values;
    }

    public void addServices_value(Services_value services_value) {
        this.services_values.add(services_value);
    }
    public services_ServiceUser getServices_serviceuser() {
        return services_serviceuser;
    }

    public void setServices_serviceuser(services_ServiceUser services_serviceuser) {
        this.services_serviceuser = services_serviceuser;
    }

}