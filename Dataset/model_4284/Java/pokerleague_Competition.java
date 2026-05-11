




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class pokerleague_Competition extends DescribedEntity {

    private int minimalAttendance;
    private LocalDate endDate;
    private int defaultMaxPlayers;
    private int defaultBuyIn;
    private LocalDate startDate;
    private int defaultTournamentAnnouncementLead;
    private int defaultMinPlayers;





    private List<pokerleague_Player> pokerleague_players;




    private pokerleague_PrizeMoneyRuleSet pokerleague_prizemoneyruleset;




    private pokerleague_Tournament pokerleague_tournament;




    private List<pokerleague_Tournament> pokerleague_tournaments;


    public pokerleague_Competition(
        int minimalAttendance,        LocalDate endDate,        int defaultMaxPlayers,        int defaultBuyIn,        LocalDate startDate,        int defaultTournamentAnnouncementLead,        int defaultMinPlayers    ) {
        super(
        );
        this.minimalAttendance = minimalAttendance;
        this.endDate = endDate;
        this.defaultMaxPlayers = defaultMaxPlayers;
        this.defaultBuyIn = defaultBuyIn;
        this.startDate = startDate;
        this.defaultTournamentAnnouncementLead = defaultTournamentAnnouncementLead;
        this.defaultMinPlayers = defaultMinPlayers;
        this.pokerleague_players = new ArrayList<>();
        this.pokerleague_tournaments = new ArrayList<>();
    }

    public pokerleague_Competition(
        int minimalAttendance,        LocalDate endDate,        int defaultMaxPlayers,        int defaultBuyIn,        LocalDate startDate,        int defaultTournamentAnnouncementLead,        int defaultMinPlayers        ArrayList<pokerleague_Player> pokerleague_players,        ArrayList<pokerleague_Tournament> pokerleague_tournaments    ) {
        this.minimalAttendance = minimalAttendance;
        this.endDate = endDate;
        this.defaultMaxPlayers = defaultMaxPlayers;
        this.defaultBuyIn = defaultBuyIn;
        this.startDate = startDate;
        this.defaultTournamentAnnouncementLead = defaultTournamentAnnouncementLead;
        this.defaultMinPlayers = defaultMinPlayers;
        this.pokerleague_players = pokerleague_players;
        this.pokerleague_tournaments = pokerleague_tournaments;
    }

    public int getMinimalattendance() {
        return minimalAttendance;
    }

    public void setMinimalattendance(int minimalAttendance) {
        this.minimalAttendance = minimalAttendance;
    }
    public LocalDate getEnddate() {
        return endDate;
    }

    public void setEnddate(LocalDate endDate) {
        this.endDate = endDate;
    }
    public int getDefaultmaxplayers() {
        return defaultMaxPlayers;
    }

    public void setDefaultmaxplayers(int defaultMaxPlayers) {
        this.defaultMaxPlayers = defaultMaxPlayers;
    }
    public int getDefaultbuyin() {
        return defaultBuyIn;
    }

    public void setDefaultbuyin(int defaultBuyIn) {
        this.defaultBuyIn = defaultBuyIn;
    }
    public LocalDate getStartdate() {
        return startDate;
    }

    public void setStartdate(LocalDate startDate) {
        this.startDate = startDate;
    }
    public int getDefaulttournamentannouncementlead() {
        return defaultTournamentAnnouncementLead;
    }

    public void setDefaulttournamentannouncementlead(int defaultTournamentAnnouncementLead) {
        this.defaultTournamentAnnouncementLead = defaultTournamentAnnouncementLead;
    }
    public int getDefaultminplayers() {
        return defaultMinPlayers;
    }

    public void setDefaultminplayers(int defaultMinPlayers) {
        this.defaultMinPlayers = defaultMinPlayers;
    }

    public List<pokerleague_Player> getPokerleague_players() {
        return pokerleague_players;
    }

    public void addPokerleague_player(Pokerleague_player pokerleague_player) {
        this.pokerleague_players.add(pokerleague_player);
    }
    public pokerleague_PrizeMoneyRuleSet getPokerleague_prizemoneyruleset() {
        return pokerleague_prizemoneyruleset;
    }

    public void setPokerleague_prizemoneyruleset(pokerleague_PrizeMoneyRuleSet pokerleague_prizemoneyruleset) {
        this.pokerleague_prizemoneyruleset = pokerleague_prizemoneyruleset;
    }
    public pokerleague_Tournament getPokerleague_tournament() {
        return pokerleague_tournament;
    }

    public void setPokerleague_tournament(pokerleague_Tournament pokerleague_tournament) {
        this.pokerleague_tournament = pokerleague_tournament;
    }
    public List<pokerleague_Tournament> getPokerleague_tournaments() {
        return pokerleague_tournaments;
    }

    public void addPokerleague_tournament(Pokerleague_tournament pokerleague_tournament) {
        this.pokerleague_tournaments.add(pokerleague_tournament);
    }

}