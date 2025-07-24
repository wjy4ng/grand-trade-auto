"use client";

import { useState } from "react";
import "./App.css";
import { Toaster, toast } from "sonner";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import {
  Popover,
  PopoverContent,
  PopoverTrigger,
} from "@/components/ui/popover";

function App() {
  const [manufacturer, setManufacturer] = useState("");
  const [model, setModel] = useState("");
  const [year, setYear] = useState("");
  const [mileage, setMileage] = useState("");

  const handleSubmit = async () => {
    const data = {
      manufacturer,
      model,
      year,
      mileage,
    };

    try {
      const response = await fetch(
        "http://13.49.27.160/api/predict-price/predict/",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(data),
        }
      );

      if (!response.ok) throw new Error("서버 오류");

      const result = await response.json();
      let carPrice = Math.floor(result.predicted_price);
      toast(`예상 차량 가격: ${carPrice} 만원`);
    } catch (err) {
      console.log(err);
      toast("오류", {
        description: "서버와 통신 중 오류가 발생했습니다.",
      });
    }
  };

  return (
    <>
      <Toaster richColors position="top-center" />
      <div className="flex flex-col justify-center items-center h-screen gap-8">
        <div className="text-center">
          <h1 className="text-2xl font-bold">Grand Trade Auto</h1>
          <p>AI 기반 중고차 가격 예측 서비스</p>
        </div>
        <Popover>
          <PopoverTrigger asChild>
            <Button variant="outline">차량 정보 입력</Button>
          </PopoverTrigger>

          <PopoverContent className="w-80">
            <div className="grid gap-4">
              <div className="space-y-2">
                <h4 className="leading-none font-medium">차량 정보</h4>
              </div>
              <div className="grid gap-2">
                <div className="grid grid-cols-3 items-center gap-4">
                  <Label htmlFor="manufacturer">제조사</Label>
                  <Input
                    id="manufacturer"
                    value={manufacturer}
                    onChange={(e) => setManufacturer(e.target.value)}
                    placeholder="ex) BMW"
                    className="col-span-2 h-8"
                  />
                </div>
                <div className="grid grid-cols-3 items-center gap-4">
                  <Label htmlFor="model">모델명</Label>
                  <Input
                    id="model"
                    value={model}
                    onChange={(e) => setModel(e.target.value)}
                    placeholder="ex) X5 (G05) xDrive 40i xLine"
                    className="col-span-2 h-8"
                  />
                </div>
                <div className="grid grid-cols-3 items-center gap-4">
                  <Label htmlFor="year">연식</Label>
                  <Input
                    id="year"
                    value={year}
                    onChange={(e) => setYear(e.target.value)}
                    placeholder="ex) 23"
                    className="col-span-2 h-8"
                  />
                </div>
                <div className="grid grid-cols-3 items-center gap-4">
                  <Label htmlFor="mileage">주행거리</Label>
                  <Input
                    id="mileage"
                    value={mileage}
                    onChange={(e) => setMileage(e.target.value)}
                    placeholder="ex) 24324"
                    className="col-span-2 h-8"
                  />
                </div>
              </div>
            </div>

            <Button
              variant="outline"
              className="mt-4 w-full"
              onClick={handleSubmit}
            >
              적용
            </Button>
          </PopoverContent>
        </Popover>
      </div>
    </>
  );
}

export default App;
