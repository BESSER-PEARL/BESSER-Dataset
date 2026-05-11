





import java.util.List;
import java.util.ArrayList;

public class RDM_RailwayDomainModel  {






    private List<RDM_ConnectionPoint> rdm_connectionpoints;




    private List<RDM_Signal> rdm_signals;




    private List<RDM_RouteElement> rdm_routeelements;




    private List<RDM_Section> rdm_sections;




    private List<RDM_Train> rdm_trains;




    private List<RDM_Route> rdm_routes;




    private List<RDM_Turnout> rdm_turnouts;




    private List<RDM_TurnoutDesiredDirection> rdm_turnoutdesireddirections;


    public RDM_RailwayDomainModel(
    ) {
        this.rdm_connectionpoints = new ArrayList<>();
        this.rdm_signals = new ArrayList<>();
        this.rdm_routeelements = new ArrayList<>();
        this.rdm_sections = new ArrayList<>();
        this.rdm_trains = new ArrayList<>();
        this.rdm_routes = new ArrayList<>();
        this.rdm_turnouts = new ArrayList<>();
        this.rdm_turnoutdesireddirections = new ArrayList<>();
    }

    public RDM_RailwayDomainModel(
        ArrayList<RDM_ConnectionPoint> rdm_connectionpoints,        ArrayList<RDM_Signal> rdm_signals,        ArrayList<RDM_RouteElement> rdm_routeelements,        ArrayList<RDM_Section> rdm_sections,        ArrayList<RDM_Train> rdm_trains,        ArrayList<RDM_Route> rdm_routes,        ArrayList<RDM_Turnout> rdm_turnouts,        ArrayList<RDM_TurnoutDesiredDirection> rdm_turnoutdesireddirections    ) {
        this.rdm_connectionpoints = rdm_connectionpoints;
        this.rdm_signals = rdm_signals;
        this.rdm_routeelements = rdm_routeelements;
        this.rdm_sections = rdm_sections;
        this.rdm_trains = rdm_trains;
        this.rdm_routes = rdm_routes;
        this.rdm_turnouts = rdm_turnouts;
        this.rdm_turnoutdesireddirections = rdm_turnoutdesireddirections;
    }


    public List<RDM_ConnectionPoint> getRdm_connectionpoints() {
        return rdm_connectionpoints;
    }

    public void addRdm_connectionpoint(Rdm_connectionpoint rdm_connectionpoint) {
        this.rdm_connectionpoints.add(rdm_connectionpoint);
    }
    public List<RDM_Signal> getRdm_signals() {
        return rdm_signals;
    }

    public void addRdm_signal(Rdm_signal rdm_signal) {
        this.rdm_signals.add(rdm_signal);
    }
    public List<RDM_RouteElement> getRdm_routeelements() {
        return rdm_routeelements;
    }

    public void addRdm_routeelement(Rdm_routeelement rdm_routeelement) {
        this.rdm_routeelements.add(rdm_routeelement);
    }
    public List<RDM_Section> getRdm_sections() {
        return rdm_sections;
    }

    public void addRdm_section(Rdm_section rdm_section) {
        this.rdm_sections.add(rdm_section);
    }
    public List<RDM_Train> getRdm_trains() {
        return rdm_trains;
    }

    public void addRdm_train(Rdm_train rdm_train) {
        this.rdm_trains.add(rdm_train);
    }
    public List<RDM_Route> getRdm_routes() {
        return rdm_routes;
    }

    public void addRdm_route(Rdm_route rdm_route) {
        this.rdm_routes.add(rdm_route);
    }
    public List<RDM_Turnout> getRdm_turnouts() {
        return rdm_turnouts;
    }

    public void addRdm_turnout(Rdm_turnout rdm_turnout) {
        this.rdm_turnouts.add(rdm_turnout);
    }
    public List<RDM_TurnoutDesiredDirection> getRdm_turnoutdesireddirections() {
        return rdm_turnoutdesireddirections;
    }

    public void addRdm_turnoutdesireddirection(Rdm_turnoutdesireddirection rdm_turnoutdesireddirection) {
        this.rdm_turnoutdesireddirections.add(rdm_turnoutdesireddirection);
    }

}