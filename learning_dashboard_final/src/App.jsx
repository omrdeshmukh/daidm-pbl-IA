import React, { useEffect, useState } from "react";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "./components/ui/tabs";
import { Card, CardContent } from "./components/ui/card";
import { BarChart as BarIcon, PieChart, Table } from "lucide-react";
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer } from "recharts";
import dataCSV from "../learning_app_survey_synthetic.csv";

export default function LearningDashboard() {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch(dataCSV)
      .then(response => response.text())
      .then(csvText => {
        const lines = csvText.split('\n');
        const headers = lines[0].split(',');
        const rows = lines.slice(1).map(line => {
          const values = line.split(',');
          return headers.reduce((acc, header, i) => ({ ...acc, [header]: values[i] }), {});
        });
        setData(rows);
      });
  }, []);

  const ageGroups = {};
  data.forEach(d => {
    const age = parseInt(d.Age);
    const group = age < 20 ? "<20" : age < 25 ? "20–24" : age < 30 ? "25–29" : "30+";
    ageGroups[group] = (ageGroups[group] || 0) + 1;
  });

  const motivations = {};
  data.forEach(d => {
    motivations[d.LearningMotivation] = (motivations[d.LearningMotivation] || 0) + 1;
  });

  const ageData = Object.entries(ageGroups).map(([k, v]) => ({ name: k, count: v }));
  const motivationData = Object.entries(motivations).map(([k, v]) => ({ name: k, count: v }));

  return (
    <main className="p-4 max-w-6xl mx-auto">
      <h1 className="text-3xl font-bold mb-6">📚 Learning Path Optimizer Dashboard</h1>
      <Tabs defaultValue="visualization" className="w-full">
        <TabsList className="grid grid-cols-3 gap-2 bg-muted p-2 rounded-xl mb-4">
          <TabsTrigger value="visualization"><BarIcon className="w-4 h-4 mr-2" /> Data Visualization</TabsTrigger>
          <TabsTrigger value="classification"><Table className="w-4 h-4 mr-2" /> Classification</TabsTrigger>
          <TabsTrigger value="regression"><Table className="w-4 h-4 mr-2" /> Regression</TabsTrigger>
        </TabsList>

        <TabsContent value="visualization">
          <Card className="mt-2">
            <CardContent className="p-6">
              <h2 className="text-xl font-semibold mb-4">Age Distribution</h2>
              <ResponsiveContainer width="100%" height={300}>
                <BarChart data={ageData}>
                  <XAxis dataKey="name" />
                  <YAxis />
                  <Tooltip />
                  <Bar dataKey="count" fill="#4f46e5" />
                </BarChart>
              </ResponsiveContainer>

              <h2 className="text-xl font-semibold mt-10 mb-4">Learning Motivations</h2>
              <ResponsiveContainer width="100%" height={300}>
                <BarChart data={motivationData}>
                  <XAxis dataKey="name" />
                  <YAxis />
                  <Tooltip />
                  <Bar dataKey="count" fill="#10b981" />
                </BarChart>
              </ResponsiveContainer>
            </CardContent>
          </Card>
        </TabsContent>

        <TabsContent value="classification">
          <Card><CardContent className="p-6">Classification models can be integrated here.</CardContent></Card>
        </TabsContent>

        <TabsContent value="regression">
          <Card><CardContent className="p-6">Regression models can be visualized here.</CardContent></Card>
        </TabsContent>
      </Tabs>
    </main>
  );
}
