





import java.util.List;
import java.util.ArrayList;

public class traceSystem_Events_Events  {






    private List<Activity_initializeExitEventOccurrence> activity_initializeexiteventoccurrences;




    private List<Activity_runNodesEntryEventOccurrence> activity_runnodesentryeventoccurrences;




    private List<Activity_runEntryEventOccurrence> activity_runentryeventoccurrences;




    private List<Activity_runExitEventOccurrence> activity_runexiteventoccurrences;




    private List<Activity_runNodesExitEventOccurrence> activity_runnodesexiteventoccurrences;


    public traceSystem_Events_Events(
    ) {
        this.activity_initializeexiteventoccurrences = new ArrayList<>();
        this.activity_runnodesentryeventoccurrences = new ArrayList<>();
        this.activity_runentryeventoccurrences = new ArrayList<>();
        this.activity_runexiteventoccurrences = new ArrayList<>();
        this.activity_runnodesexiteventoccurrences = new ArrayList<>();
    }

    public traceSystem_Events_Events(
        ArrayList<Activity_initializeExitEventOccurrence> activity_initializeexiteventoccurrences,        ArrayList<Activity_runNodesEntryEventOccurrence> activity_runnodesentryeventoccurrences,        ArrayList<Activity_runEntryEventOccurrence> activity_runentryeventoccurrences,        ArrayList<Activity_runExitEventOccurrence> activity_runexiteventoccurrences,        ArrayList<Activity_runNodesExitEventOccurrence> activity_runnodesexiteventoccurrences    ) {
        this.activity_initializeexiteventoccurrences = activity_initializeexiteventoccurrences;
        this.activity_runnodesentryeventoccurrences = activity_runnodesentryeventoccurrences;
        this.activity_runentryeventoccurrences = activity_runentryeventoccurrences;
        this.activity_runexiteventoccurrences = activity_runexiteventoccurrences;
        this.activity_runnodesexiteventoccurrences = activity_runnodesexiteventoccurrences;
    }


    public List<Activity_initializeExitEventOccurrence> getActivity_initializeexiteventoccurrences() {
        return activity_initializeexiteventoccurrences;
    }

    public void addActivity_initializeexiteventoccurrence(Activity_initializeexiteventoccurrence activity_initializeexiteventoccurrence) {
        this.activity_initializeexiteventoccurrences.add(activity_initializeexiteventoccurrence);
    }
    public List<Activity_runNodesEntryEventOccurrence> getActivity_runnodesentryeventoccurrences() {
        return activity_runnodesentryeventoccurrences;
    }

    public void addActivity_runnodesentryeventoccurrence(Activity_runnodesentryeventoccurrence activity_runnodesentryeventoccurrence) {
        this.activity_runnodesentryeventoccurrences.add(activity_runnodesentryeventoccurrence);
    }
    public List<Activity_runEntryEventOccurrence> getActivity_runentryeventoccurrences() {
        return activity_runentryeventoccurrences;
    }

    public void addActivity_runentryeventoccurrence(Activity_runentryeventoccurrence activity_runentryeventoccurrence) {
        this.activity_runentryeventoccurrences.add(activity_runentryeventoccurrence);
    }
    public List<Activity_runExitEventOccurrence> getActivity_runexiteventoccurrences() {
        return activity_runexiteventoccurrences;
    }

    public void addActivity_runexiteventoccurrence(Activity_runexiteventoccurrence activity_runexiteventoccurrence) {
        this.activity_runexiteventoccurrences.add(activity_runexiteventoccurrence);
    }
    public List<Activity_runNodesExitEventOccurrence> getActivity_runnodesexiteventoccurrences() {
        return activity_runnodesexiteventoccurrences;
    }

    public void addActivity_runnodesexiteventoccurrence(Activity_runnodesexiteventoccurrence activity_runnodesexiteventoccurrence) {
        this.activity_runnodesexiteventoccurrences.add(activity_runnodesexiteventoccurrence);
    }

}